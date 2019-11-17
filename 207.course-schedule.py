#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (38.33%)
# Total Accepted:    229.3K
# Total Submissions: 598.2K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#
class GraphVertex:
        WHITE, GREY, BLACK = range(3)
        def __init__(self, edges):
            self.edges = edges
            self.color = GraphVertex.WHITE

class Solution:
    def canFinish(self, numCourses, prerequisites):
        def has_cycle(cur, graph):
            if cur.color == GraphVertex.GREY:
                return True

            cur.color = GraphVertex.GREY

            if any(graph[next_vertex].color != GraphVertex.BLACK and has_cycle(graph[next_vertex], graph) for next_vertex in cur.edges):
                return True

            cur.color = GraphVertex.BLACK
            
            return False

        graph = {}
        for prereq in prerequisites:
            if prereq[1] in graph:
                graph[prereq[1]].edges.append(prereq[0])

            else:
                graph[prereq[1]] = GraphVertex([prereq[0]])
                
            if prereq[0] not in graph:
                graph[prereq[0]] = GraphVertex([])

        return not any(graph[vertex].color == GraphVertex.WHITE and has_cycle(graph[vertex], graph) for vertex in graph.keys())
