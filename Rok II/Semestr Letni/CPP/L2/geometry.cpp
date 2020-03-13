#include "geometry.h"

Vector::Vector(double dx, double dy){
    dx = dx;
    dy = dy;
}

Vector::Vector(const Vector &vec){
    dx = vec.dx;
    dy = vec.dy;
}

Point::Point(double x, double y){
    x = x;
    y = y;
}

Point::Point(const Point &p, const Vector &vec){
    x = p.x + vec.dx;
    y = p.y + vec.dy;
}

Point::Point(const Point &p){
    x = p.x;
    y = p.y;
}

double Line::getA() const{
    return a;
}

double Line::getB() const {
    return b;
}

double Line::getC() const {
    return c;
}

Line::Line(const Point &p, const Point &q){
    double oa, ob, oc;
    oa = q.y - p.y;
    ob = p.x - q.x;
    oc = q.x * p.y - p.x * q.y;

    double mi;
    mi = sqrt(oa * oa + ob * ob);
    a = oa / mi;
    b = ob / mi;
    c = oc / mi;
}

Line::Line(const Vector &vec){
    double oa, ob, mi;
    oa = vec.dx;
    ob = vec.dy;
    mi = sqrt(oa * oa + ob * ob);
    a = oa / mi;
    b = ob / mi;
    c = -a * vec.dx - b * vec.dy;
}

Line::Line(double a, double b, double c){
    double mi;
    mi = sqrt(a * a + b * b);
    a = a / mi;
    b = b / mi;
    c = c / mi;
}

Line::Line(const Line &l, const Vector &vec){
    double oa, ob, oc, mi;
    oa = l.getA() / l.getB();
    ob = 1;
    oc = l.getC() / l.getB() - vec.dy - l.getA()/l.getB() * vec.dx;
    mi = sqrt(oa * oa + ob * ob);
    a = oa / mi;
    b = ob / mi;
    c = oc / mi;
}

bool Line::vecParallel(const Vector vec){
    return vec.dx == -b && vec.dy == a;
}
 
bool Line::vecPerpendicular(const Vector vec){
    return vec.dx == a && vec.dy == b;
}

bool Line::pointIn(const Point p){
    return a * p.x + b * p.y + c == 0;
}

Vector Add(const Vector vec1, const Vector vec2){
    return Vector(vec1.dx + vec2.dx, vec1.dy + vec2.dy);
}

bool Parallel (const Line &l1, const Line &l2){
    return l1.getA() * l2.getB() == l1.getB() * l2.getA();
}

bool Perpendicular (const Line &l1, const Line &l2){
    return l1.getA() * l2.getA() == -1 * l1.getB() * l2.getB();
}

Point Crossing(const Line &l1, const Line &l2){
    double wx = 0;
	double wy = 0;
	double w = 1;
    w = l1.getA() * l2.getB() - l2.getA() * l1.getB();
    wx = -1 * l1.getC() * l2.getB() + l2.getC() * l1.getB();
    wy = -1 * l1.getA() * l2.getC() + l2.getA() * l1.getC();

    return Point(wx/w, wy/w);
}