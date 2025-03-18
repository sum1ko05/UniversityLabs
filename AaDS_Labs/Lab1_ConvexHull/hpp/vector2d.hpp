#pragma once
#include "../hpp/point2d.hpp"
#include <iostream>
#define realnum double

namespace space2d
{
	class Vector2d
	{
	public:
		//Defining vector with coordinated - don't stick with points 
		realnum x;
		realnum y;

	private:
		void swap(Vector2d& other);
	public:
		Vector2d();
		Vector2d(realnum X, realnum Y);
		Vector2d(Point2d start, Point2d end);

		//Rule of three
		Vector2d(const Vector2d& other); //Copy constructor
		Vector2d& operator=(Vector2d copy); //Copy operator
		~Vector2d(); //Destructor

		//Operations
		realnum length();
		realnum polar_arg();
		bool operator==(Vector2d& other);
		bool operator!=(Vector2d& other);
		bool operator||(Vector2d& other);
		Vector2d operator-();
		Vector2d operator+(Vector2d& other);
		Vector2d& operator+=(Vector2d& other);
		Vector2d operator-(Vector2d& other);
		Vector2d& operator-=(Vector2d& other);
		Vector2d operator*(realnum& other);
		Vector2d& operator*=(realnum& other);

		//IO streams
		friend std::istream& operator>>(std::istream& in, Vector2d& vector)
		{
			in >> vector.x >> vector.y;
			return in;
		}
		friend std::ostream& operator<<(std::ostream& out, const Vector2d& vector)
		{
			out << "{" << vector.x << ", " << vector.y << "}";
			return out;
		}
	};
}