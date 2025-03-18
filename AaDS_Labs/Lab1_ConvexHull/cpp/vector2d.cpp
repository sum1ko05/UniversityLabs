#include "../hpp/vector2d.hpp"
#include "../hpp/point2d.hpp"
#include "iostream"
#include <math.h>
#define pi 3.14159265359
#define realnum double
#define epsilon 0.000001

namespace space2d
{
	void Vector2d::swap(Vector2d& other)
	{
		std::swap(x, other.x);
		std::swap(y, other.y);
	}
	//Basic constructor
	Vector2d::Vector2d(realnum X, realnum Y)
	{
		x = X;
		y = Y;
	}
	Vector2d::Vector2d(Point2d start, Point2d end)
	{
		x = end.x - start.x;
		y = end.y - start.y;
	}
	Vector2d::Vector2d()
	{
		x = 0;
		y = 0;
	}

	//Copy constructor
	Vector2d::Vector2d(const Vector2d& other)
	{
		x = other.x;
		y = other.y;
	}
	//Copy constructor
	Vector2d& Vector2d::operator=(Vector2d copy)
	{
		swap(copy);
		return *this;
	}
	//Destructor
	Vector2d::~Vector2d()
	{

	}

	//Operations
	realnum Vector2d::length()
	{
		return sqrt((x * x) + (y * y)); //Assuming that we use |i|=|j|=1, i*j=0 as basis
	}
	realnum Vector2d::polar_arg() //Seeking for angle in [-pi, pi)
	{
		if (x > 0) return std::atan(y / x);
		if (x < 0)
		{
			if (y >= 0)  return std::atan(y / x) + pi;
			if (y < 0)  return std::atan(y / x) - pi;
		}
		//x = 0 - dividing isn't suitable here
		if (y > 0) return (pi / 2);
		else return -(pi / 2);

	}
	bool Vector2d::operator==(Vector2d& other)
	{
		return (abs(x - other.x) < epsilon) && (abs(y - other.y) < epsilon); // |x-y|<e => x~y with e precision
	}
	bool Vector2d::operator!=(Vector2d& other)
	{
		return !(*this == other);
	}
	bool Vector2d::operator||(Vector2d& other)
	{
		return abs((x / y) - (other.x / other.y)) < epsilon; // |x-y|<e => x~y with e precision
	}
	Vector2d Vector2d::operator-()
	{
		return Vector2d(-x, -y);
	}
	Vector2d Vector2d::operator+(Vector2d& other)
	{
		return Vector2d(x + other.x, y + other.y);
	}
	Vector2d& Vector2d::operator+=(Vector2d& other)
	{
		Vector2d tmp = *this + other;
		*this = tmp;
		return *this;
	}
	Vector2d Vector2d::operator-(Vector2d& other)
	{
		return Vector2d(x - other.x, y - other.y);
	}
	Vector2d& Vector2d::operator-=(Vector2d& other)
	{
		Vector2d tmp = *this - other;
		*this = tmp;
		return *this;
	}
	Vector2d Vector2d::operator*(realnum& other)
	{
		return Vector2d(x * other, y * other);
	}
	Vector2d& Vector2d::operator*=(realnum& other)
	{
		Vector2d tmp = *this * other;
		*this = tmp;
		return *this;
	}
}