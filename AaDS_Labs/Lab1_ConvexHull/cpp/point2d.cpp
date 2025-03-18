#include "../hpp/point2d.hpp"
#include "iostream"
#define realnum double
#define epsilon 0.000001

namespace space2d
{
	void Point2d::swap(Point2d& other)
	{
		std::swap(x, other.x);
		std::swap(y, other.y);
	}
	//Basic constructor
	Point2d::Point2d(realnum X, realnum Y)
	{
		x = X;
		y = Y;
	}
	Point2d::Point2d()
	{
		x = 0;
		y = 0;
	}

	//Copy constructor
	Point2d::Point2d(const Point2d& other)
	{
		x = other.x;
		y = other.y;
	}
	//Copy constructor
	Point2d& Point2d::operator=(Point2d copy)
	{
		swap(copy);
		return *this;
	}
	//Destructor
	Point2d::~Point2d()
	{
		
	}

	//Operations
	bool Point2d::operator==(Point2d& other)
	{
		return (abs(x - other.x) < epsilon) && (abs(y - other.y) < epsilon); // |x-y|<e => x~y with e precision
	}
	bool Point2d::operator!=(Point2d& other)
	{
		return !(*this == other);
	}
}