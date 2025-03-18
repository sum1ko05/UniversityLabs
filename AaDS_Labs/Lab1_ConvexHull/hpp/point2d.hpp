#pragma once
#include <iostream>
#define realnum double

namespace space2d
{
	class Point2d
	{
	public:
		realnum x;
		realnum y;

	private:
		void swap(Point2d& other);
	public:
		Point2d();
		Point2d(realnum X, realnum Y);

		//Rule of three
		Point2d(const Point2d& other); //Copy constructor
		Point2d& operator=(Point2d copy); //Copy operator
		~Point2d(); //Destructor

		//Operations
		bool operator==(Point2d& other);
		bool operator!=(Point2d& other);

		//IO streams
		friend std::istream& operator>>(std::istream& in, Point2d& point)
		{
			in >> point.x >> point.y;
			return in;
		}
		friend std::ostream& operator<<(std::ostream& out, const Point2d& point)
		{
			out << "(" << point.x << ", " << point.y << ")";
			return out;
		}
	};
}