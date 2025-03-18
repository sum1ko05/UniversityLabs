#include "../hpp/line2d.hpp"
#include "../hpp/vector2d.hpp"
#include "../hpp/point2d.hpp"
#include "iostream"
#include <math.h>
#define pi 3.14159265359
#define realnum double
#define epsilon 0.000001

namespace space2d
{
	void Line2d::swap(Line2d& other)
	{
		std::swap(init_point, other.init_point);
		std::swap(direct_vector, other.direct_vector);
	}
	//Basic constructor
	Line2d::Line2d(Point2d start, Point2d end)
	{
		init_point = start;
		direct_vector = Vector2d(start, end);
	}
	Line2d::Line2d(Point2d start, Vector2d direction)
	{
		init_point = start;
		direct_vector = direction;
	}
	Line2d::Line2d()
	{
		init_point = Point2d(0, 0);
		direct_vector = Vector2d(1, 0);
	}

	//Copy constructor
	Line2d::Line2d(const Line2d& other)
	{
		init_point = other.init_point;
		direct_vector = other.direct_vector;
	}
	//Copy constructor
	Line2d& Line2d::operator=(Line2d copy)
	{
		swap(copy);
		return *this;
	}
	//Destructor
	Line2d::~Line2d()
	{

	}

	//Operations
	bool Line2d::operator||(Line2d& other)
	{
		return direct_vector || other.direct_vector;
	}
	bool Line2d::operator==(Line2d& other)
	{
		return (direct_vector || other.direct_vector) && (init_point == other.init_point);
	}
	bool Line2d::operator>(Point2d& other)
	{
		return Vector2d(init_point, other) || direct_vector;
	}
	/*
	* Let init point as (x0, y0) and direct vector as {p1, p2}
	* "Canonical" equation: (x - x0)/p1 = (y - y0)/p2
	* We don't want to deal with dividing by zero and we need to use it for calculations
	* Common equation: p2(x) - p1(y) + (p1(y0) - p2(x0)) = 0
	* After variable changing: Ax + By + C = 0, where A = p2, B = -p1, C = p1(y0) - p2(x0)
	* To find intersection we should solve system of equations:
	* 2 lines: A1x + B1y + C1 = 0, A2x + B2y + C2 = 0
	* The system: { A1x + B1y = -C1
	*			  { A2x + B2y = -C2
	* We can use Cramer's rule since it's not suitable only for infinite solutions (equal lines)
	* or no solutions (parallel lines), and we can just raise exception for these cases
	*/
	Point2d Line2d::operator^(Line2d& other)
	{
		if (direct_vector || other.direct_vector) std::exception("Parallel or equal lines");
		//I just don't want to be confused in calculations
		realnum A1 = direct_vector.y; realnum B1 = -direct_vector.x; 
		realnum C1 = (direct_vector.x * init_point.y) - (direct_vector.y * init_point.x);
		realnum A2 = other.direct_vector.y; realnum B2 = -other.direct_vector.x;
		realnum C2 = (other.direct_vector.x * other.init_point.y) - (other.direct_vector.y * other.init_point.x);
		realnum main_det = (A1 * B2) - (B1 * A2); //We already excluded cases, where main_det could possibly be 0
		realnum det1 = (-C1 * B2) - (B1 * -C2);
		realnum det2 = (A1 * -C2) - (-C1 * A2);
		Point2d intersection = Point2d(det1/main_det, det2/main_det);
		return intersection;
	}
}