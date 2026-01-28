
import { React, useEffect, useState } from "react";
import { getCourses } from "../services/courseService";

function Courses() {

    const [courses, setCourses] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchCourses() {
            const cs = await getCourses();
            console.log(cs);
            
            setCourses(cs);
            setLoading(false);
        }
        fetchCourses();
    }, []);

    if(loading){
        return <div>Loading...</div>;
    }

    return (
        <div className="my-6 px-12">
            <h2 className="font-bold text-2xl">Courses Page</h2>
            <div className="my-6">
                {courses.length === 0 ? (<p>No courses available</p>) : (
                    <div className="flex gap-4 ">
                        {courses.map(course => (
                            <div key={course.id} className="p-3 rounded-md bg-gray-100 w-[250px]">
                                <div className="font-bold">{course.title}</div>
                                <div className="text-sm">{course.description}</div>
                                <a className="text-blue-600 underline" href={`/courses/${course.id}`}>View Details</a>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

export default Courses;