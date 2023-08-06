from operator import itemgetter

import pandas as pd
import networkx as nx

from tennisrank.model import Player, PlayerRank
from tennisrank.utils import fuzzy_match


class MatchGraphBuilder:
    """
    Main class for building graph
    """

    def __init__(self, matches):
        self._matches = matches

    def get_bias(self, matches):
        df = pd.DataFrame(matches)
        if df['point_diff'].min() < 1:
            return abs(df['point_diff'].min()) + 1
        else:
            return 0

    def get_multigraph(self, point_diff=True):
        """Return graph as multigraph

        Args:
            point_diff (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        G = nx.MultiDiGraph()
        for player in self._get_players():
            G.add_node(player.id, name=player.name)
        for m in self._matches:
            weight = m.point_diff if point_diff else 1
            G.add_edge(m.loser.id, m.winner.id, weight=weight)
        return G

    def get_digraph(self, point_diff=True):
        """Return graph as directed graph

        Args:
            point_diff (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        G = self.get_multigraph(point_diff=point_diff)
        H = nx.DiGraph()
        for u, v, d in G.edges(data=True):
            # use point_diff if weighted
            w = d['weight']
            if H.has_edge(u, v):
                H[u][v]['weight'] += w
            else:
                H.add_edge(u, v, weight=w)
        return H

    def _get_players(self):
        def iter_players():
            for m in self._matches:
                yield m.winner
                yield m.loser
        return set(iter_players())


class TennisRank:
    """Ranking algorithm
    """

    def __init__(self, matches):
        self._matches = matches

    def _get_named_ids(self, matches):
        named_ids = {}
        for m in matches:
            named_ids[m.winner.id] = m.winner.name
            named_ids[m.loser.id] = m.loser.name
        return named_ids

    def _filter_matches(self, surface='all'):
        return [match for match in self._matches
                if match.surface == surface or surface == 'all']

    def get_ranks(self, point_diff=False, surface='all', alpha=0.9):
        filt_matches = self._filter_matches(surface)
        named_ids = self._get_named_ids(filt_matches)
        G = MatchGraphBuilder(filt_matches).get_digraph(point_diff=point_diff)
        if point_diff:
            pageranks = nx.pagerank(G, alpha=alpha, weight='weight')
        else:
            pageranks = nx.pagerank(G, alpha=alpha, weight='weight')
        # make sure pageranks are sorted
        pageranks = sorted(
            [(pid, pagerank) for pid, pagerank in pageranks.items()],
            key=lambda x: x[1],
            reverse=True
        )
        return [
            PlayerRank(
                player=Player(id=pid, name=named_ids[pid]),
                rank=i+1,
                surface=surface
            )
            for i, (pid, _)
            in enumerate(pageranks)
        ]
    
    def get_rank(self, player, point_diff=False, surface='all', alpha=0.9):
        player_name = player.name if type(player) == Player else player
        ranks = self.get_ranks(point_diff=point_diff, surface=surface, alpha=alpha)
        fuzz = [
            (pr, fuzzy_match(pr.player.name.lower(), player_name.lower()))
            for pr in ranks
        ]
        if len(fuzz):
            return max(fuzz, key=itemgetter(1))

