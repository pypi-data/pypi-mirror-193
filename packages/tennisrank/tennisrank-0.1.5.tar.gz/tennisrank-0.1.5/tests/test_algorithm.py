import pdb

import networkx as nx
import pytest

from tennisrank.algorithm import MatchGraphBuilder, TennisRank
from tennisrank.model import Player, Match, PlayerRank


@pytest.fixture
def players():
    return [
        Player(id=1, name='Alice'),
        Player(id=2, name='Bob'),
        Player(id=3, name='Carol'),
        Player(id=4, name='Dan')
    ]

@pytest.fixture
def matches(players):
    return [
        Match(winner=players[0], loser=players[1], point_diff=10, surface='hard'),
        Match(winner=players[0], loser=players[1], point_diff=10, surface='hard'),
        Match(winner=players[1], loser=players[0], point_diff=3, surface='hard'),
        Match(winner=players[1], loser=players[2], point_diff=21, surface='grass'),
        Match(winner=players[2], loser=players[3], point_diff=32, surface='clay'),
        Match(winner=players[2], loser=players[3], point_diff=-4, surface='hard'),
    ]

@pytest.fixture
def graph_builder(matches):
    return MatchGraphBuilder(matches)


class TestMatchGraphBuilder:

    def test_get_same_players(self, players, graph_builder):
        computed_players = graph_builder._get_players()
        assert set(computed_players) == set(players)


    def test_get_multigraph_names(self, players, graph_builder):
        G = graph_builder.get_multigraph()
        assert type(G) == nx.MultiDiGraph
        player_names = {p.name for p in players}
        node_names = {d['name'] for n, d in G.nodes(data=True)}
        for player_name in player_names:
            assert player_name in node_names
        for node_name in node_names:
            assert node_name in player_names

    def test_get_digraph_point_diff_weights(self, graph_builder):
        G = graph_builder.get_digraph(point_diff=True)
        #pdb.set_trace()
        assert type(G) == nx.DiGraph
        # Check point diffs on all edges
        assert G.get_edge_data(2, 3) is None
        assert G.get_edge_data(3, 4) is None
        assert G.get_edge_data(2, 1)['weight'] == 20
        assert G.get_edge_data(1, 2)['weight'] == 3
        assert G.get_edge_data(3, 2)['weight'] == 21
        assert G.get_edge_data(4, 3)['weight'] == 28

    def test_get_digraph_unit_weights(self, graph_builder):
        G = graph_builder.get_digraph(point_diff=False)
        #pdb.set_trace()
        assert type(G) == nx.DiGraph
        # Check point diffs on all edges
        assert G.get_edge_data(2, 3) is None
        assert G.get_edge_data(3, 4) is None
        assert G.get_edge_data(2, 1)['weight'] == 2
        assert G.get_edge_data(1, 2)['weight'] == 1
        assert G.get_edge_data(3, 2)['weight'] == 1
        assert G.get_edge_data(4, 3)['weight'] == 2


class TestMatchGraphBuilder:

    def test_tennis_rank_all_unit(self, matches):
        tr = TennisRank(matches)
        ranks = tr.get_ranks(surface='all', point_diff=False)
        pids = [rp.player.id for rp in ranks]
        assert pids
