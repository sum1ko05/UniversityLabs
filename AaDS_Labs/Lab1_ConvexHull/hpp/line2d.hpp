#pragma once
#include "../hpp/point2d.hpp"
#include "../hpp/vector2d.hpp"
#include <iostream>
#define realnum double

namespace space2d
{
	class Line2d
	{
	//Defining line through point and free vector for line direction
	public:
		Point2d init_point;
		Vector2d direct_vector;
	private:
		void swap(Line2d& other);
	public:
		Line2d();
		Line2d(Point2d start, Vector2d direction);
		Line2d(Point2d start, Point2d end);

		//Rule of three
		Line2d(const Line2d& other); //Copy constructor
		Line2d& operator=(Line2d copy); //Copy operator
		~Line2d(); //Destructor

		//Operations
		bool operator||(Line2d& other);
		bool operator==(Line2d& other);
		bool operator>(Point2d& other); //">" is used as superset operator
		Point2d operator^(Line2d& other); //"^" is used as intersection operator
	};
}