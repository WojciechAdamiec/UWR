#include <iostream>
#include "geometry.h"


int main(){
    
	Vector v(-6, 15);
	Vector u(v);

	Point p(21, 37);
	Point q(p, v);

	Point pp = Point();
	
	Line line1(p, q);
	Line line2(u);
	Line line3(7, -3, 12);
	Line line4(line3, u);

	std::cout << v.dx << " : " << v.dy << "\n";
	std::cout << u.dx << " : " << u.dy << "\n";

	std::cout << p.x << " : " << p.y << "\n";
	std::cout << q.x << " : " << q.y << "\n";

	std::cout << pp.x << " : " << pp.y << "\n";

	std::cout << line1.getA() << " :1: " << line1.getB() << " : " << line1.getC() << "\n";
	std::cout << line2.getA() << " :2: " << line2.getB() << " : " << line2.getC() << "\n";
	std::cout << line3.getA() << " :3: " << line3.getB() << " : " << line3.getC() << "\n";
	std::cout << line4.getA() << " :4: " << line4.getB() << " : " << line4.getC() << "\n";

	Line l1(2, 2, 2);
	Line l2(4, 4, 2);
	Line l3(-4, 4, 6);

	if (Parallel(l1, l2)) {
		std::cout << "Parallel : OK!" << " \n";
	}

	if (Perpendicular(l1, l2)) {
		std::cout << "Perpendicular: Not OK!" << " \n";
	}

	if (Perpendicular(l1, l3)) {
		std::cout << "Perpendicular: OK!" << " \n";
	}

	if (Parallel(l1, l3)) {
		std::cout << "Parallel: Not OK!" << " \n";
	}

	Line l4(10, -5, 0);

	if (l4.pointIn(pp)) {
		std::cout << "PointIn: OK!" << " \n";
	}
	if (l4.pointIn(p)) {
		std::cout << "PointIn: Not OK!" << " \n";
	}

	Vector vec1(2, 4);
	Vector vec2(3, 6);

	Vector vec3 = Add(vec1, vec2);
	std::cout << "Should be 5:10 " << vec3.dx << " : " << vec3.dy << "\n";

	Line ll1(-4, 4, 0);
	Line ll2(4, 4, 4);
	
	Point ppp = Crossing(ll1, ll2);
	std::cout << "Should be: -0.5, -0.5 from geogebra: " << ppp.x << " : " << ppp.y << "\n";

	Line testl(1, 1, 0);
	Vector vv1(1, 1);
	Vector vv2(1, -1);
	
	if (testl.vecParallel(vv2)) {
		std::cout << "vecParallel: OK!" << " \n";
	}
	if (testl.vecParallel(vv1)) {
		std::cout << "vecParallel: Not OK!" << " \n";
	}
	if (testl.vecPerpendicular(vv1)) {
		std::cout << "vecPerpendicular: OK!" << " \n";
	}
	if (testl.vecPerpendicular(vv2)) {
		std::cout << "vecPerpendicular: Not OK!" << " \n";
	}

	int x;
	std::cin >> x;
    return 0;
}
