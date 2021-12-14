#pragma once
struct Vec2 {
    int x;
    int y;

    bool operator==(const Vec2 &v) const {
        return x == v.x && y == v.y;
    }
    bool operator!=(const Vec2 &v) const {
        return x != v.x || y != v.y;
    }
};

struct Node {
    double distance;
    Vec2 point;

    friend bool operator<(const Node &node, const Node &node2) {
        return node.distance < node2.distance;
    }

    friend bool operator>(const Node &node, const Node &node2) {
        return node.distance > node2.distance;
    }
};

struct Record {
    Node node;
    bool visited;
};
