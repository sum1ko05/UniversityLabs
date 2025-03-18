#include "hpp/point2d.hpp"
#include "hpp/vector2d.hpp"
#include "hpp/pointset2d.hpp"
#include "hpp/line2d.hpp"
#define realnum double

int main()
{
	space2d::Point2d p1, p2;
	space2d::Vector2d v1, v2;
	std::cin >> p1 >> v1;
	std::cin >> p2 >> v2;
	space2d::Line2d l1, l2;
	l1 = space2d::Line2d(p1, v1);
	l2 = space2d::Line2d(p2, v2);
	std::cout << space2d::Point2d(l1 ^ l2);
	return 0;
}