#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

struct point
{
    double x,y;
    
    point(double x, double y) : x(x), y(y)
    {
    }
    
    double dist2(const point& p)
    {
        return (p.x-x)*(p.x-x) + (p.y-y)*(p.y-y);
    }
    
    bool withinRangeX(double min, double max)
    {
        return x >= min && x <= max;
    }
    
    bool withinRangeY(double min, double max)
    {
        return y >= min && y <= max;
    }
};

struct point_set
{
    vector<point> points;

    //track the spatial range of the point_set
    //i.e. the axis-aligned bounding box that contains all points
    //this spatial information will be used for splitting

    double minX, maxX;
    double minY, maxY;
    
    point_set() {}
        
    void add_point(double x, double y)
    {
        if(points.size() == 0)
        {
            //initialize range
            minX = maxX = x;
            minY = maxY = y;
        }
        else
        {
            if(x < minX) minX = x;
            if(x > maxX) maxX = x;
            
            if(y < minY) minY = y;
            if(y > maxY) maxY = y;
        }
        
        points.push_back(point(x,y));
    }
    
    void add_point(const point& p)
    {
        add_point(p.x, p.y);
    }
    
    double midX()
    {
        return (minX+maxX) / 2;
    }
    
    double midY()
    {
        return (minY+maxY)/2;
    }
    
    //an open interval could have been used to prevent double including. meaning, if there is a
    //point on the splitting line, it will appear in two quadrants. this will not affect results
    point_set* getWithinRange(double minX, double minY, double maxX, double maxY)
    {
        point_set * result = new point_set();
        
        for(auto it = points.begin(); it != points.end(); ++it)
        {
            if(it->withinRangeX(minX, maxX) &&
               it->withinRangeY(minY, maxY))
            {
                result->add_point(*it);
            }
        }
        
        return result;
    }
    
    point_set* getHorizontalMargin(double height)
    {
        double hh = height/2;
        
        return getWithinRange(minX, midY()-hh, maxX, midY()+hh);
    }
    
    point_set* getVerticalMargin(double width)
    {
        double hw = width/2;
        
        return getWithinRange(midX()-hw, minY, midX()+hw, maxY);
    }
    
    point_set* getCenterSquare(double size)
    {
        double hs = size/2;
        
        return getWithinRange(midX()-hs, midY()-hs, midX()+hs, midY()+hs);
    }
    
    //bl, br, tl, tr in that order
    //or raster order, with the 3rd and 4th having the larger y values (y+ up)
    vector<point_set*> split_into_quads()
    {
        double midX = (minX+minX)/2;
        double midY = (minY+maxY)/2;
        vector<point_set*> quads;
        
        //left quads will have an openX interval.
        //bottom quads will have an openY interval.
        
        point_set* bl = getWithinRange(minX, minY, midX, midY);
        point_set* br = getWithinRange(midX, minY, maxX, midY);
        point_set* tl = getWithinRange(minX, midY, midX, maxY);
        point_set* tr = getWithinRange(midX, midY, maxX, maxY);
        
        quads.push_back(bl);
        quads.push_back(br);
        quads.push_back(tl);
        quads.push_back(tr);
        
        return quads;
    }
};

double closest_pair(point_set& ps)
{
    //base case, size of points is smaller enough to compare all pairings
    if(ps.points.size() <= 5)
    {
        double closestSq = 1e9;
        
        for(int i=0;i<ps.points.size(); ++i)
        {
            for(int j=i+1; j<ps.points.size(); ++j)
            {
                double dist2 = ps.points[i].dist2(ps.points[j]);
                
                closestSq = min(closestSq, dist2);
            }
        }
        
        return sqrt(closestSq);
    }
    
    //split point set into quadrants
    vector<point_set*> quads = ps.split_into_quads();
    
    //the prospective closest pair is the closest pair from any of the quadrants.
    double prospectiveClosest = 1e9;
    
    for(int i=0;i<4; ++i)
    {
        double closest = closest_pair(*quads[i]);
        
        prospectiveClosest = min(prospectiveClosest, closest);
    }
    
    //but of course the closest pair may be between two points in two different quadrants.
    //but if it is, it is closer than the prospective closest pair, which puts an upper
    //bound on the size of the margin we have to consider between the quadrants.
    
    //consider horizontal middle margin, centered on the midY line, height prospectiveClosest
    //consider vertical middle margin, centered on the midX line, width prospectiveClosest
    //and third, consider the corner margin, centered at midX, midY, size prospectiveClosest
    
    point_set* h_margin = ps.getHorizontalMargin(prospectiveClosest);
    point_set* v_margin = ps.getVerticalMargin(prospectiveClosest);
    point_set* center_sq = ps.getCenterSquare(prospectiveClosest);
    
    double closest = prospectiveClosest;
    
    //at the top levels, the margins may be large. this will recurse and find the closest within
    //the margins efficiently
    closest = min(closest, closest_pair(*h_margin));
    closest = min(closest, closest_pair(*v_margin));
    closest = min(closest, closest_pair(*center_sq));
    
    for(int i=0;i<4; ++i)
    {
        delete quads[i];
    }
    
    delete h_margin;
    delete v_margin;
    delete center_sq;
    
    return closest;
}

int main(int argc, char ** argv)
{
    ifstream file;
    file.open(argv[1]);

    int n;    
    
    while (file >> n)
    {
        if(n == 0) break;
        
        point_set points;
        
        for(int i=0;i<n; ++i)
        {
            double px,py;
            
            file >> px >> py;
            
            points.add_point(px,py);
        }
                    
        cout << closest_pair(points) << endl;

    }
}
