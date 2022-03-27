#pragma once
#include <math.h>

class Vector
{
    public:

    static double dx;
    static double dy;

    Vector() = default;
    Vector(double dx, double dy);
    Vector(const Vector &vec);
};

class Point
{
    public:

    static double x;
    static double y;

    Point() = default;
    Point(double x, double y);
    Point(const Point &p, const Vector &vec);
    Point(const Point &p);

};

class Line
{
    private:

    double a;
    double b;
    double c;

    public:

    double getA() const;
    double getB() const;
    double getC() const;

    Line() = default;
    Line(const Point &p, const Point &q);
    Line(const Vector &vec);
    Line(double a, double b, double c);
    Line(const Line &l, const Vector &vec);
	Line(const Line &line) = delete;

    bool vecParallel(const Vector vec);
    bool vecPerpendicular(const Vector vec);
    bool pointIn(const Point p);
};

Vector Add(const Vector vec1, const Vector vec2);
bool Parallel (const Line &l1, const Line &l2);
bool Perpendicular (const Line &l1, const Line &l2);
Point Crossing(const Line &l1, const Line &l2);
