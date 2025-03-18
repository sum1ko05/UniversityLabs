#pragma once
#include <iostream>
#include "../hpp/point2d.hpp"
#include "../hpp/vector2d.hpp"
#include <vector>
#define realnum double

namespace space2d
{
	//Convex hull approved, edit only for refactoring since no other functionality isn't planned
	class PointSet2d
	{
	public:
		std::vector<Point2d> set;

	private:
		void swap(PointSet2d& other);
		PointSet2d sort_by_angle(int index);
	public:
		PointSet2d();
		PointSet2d(std::vector<Point2d> vector);

		//Rule of three
		PointSet2d(const PointSet2d& other); //Copy constructor
		PointSet2d& operator=(PointSet2d copy); //Copy operator
		~PointSet2d(); //Destructor

		//Operations
		PointSet2d convexHull();

		//IO streams
		/* //idk how to accept points just in single line
		friend std::istream& operator>>(std::istream& in, PointSet2d& point)
		{
			in >> point.x >> point.y;
			return in;
		}
		*/
		/* //error with vector accured, stopped working on it
		friend std::ostream& operator<<(std::ostream& out, const PointSet2d& point)
		{
			st;
			return out;
		}
		*/
	};
}