import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getCourseById } from "../services/courseService";
import { getTeacherDetails } from "../services/teacherService";
import { createEnrollment } from "../services/enrollmentService";

function CourseDetails() {
    const id = useParams().id;
    const [course, setCourse] = useState(null);
    const [teacher, setTeacher] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    useEffect(() => {
        async function fetchCourseDetails() {
            const c = await getCourseById(id);
            setCourse(c);
            const teacher = await getTeacherDetails(c.teacher);
            setTeacher(teacher);
            setIsLoading(false);
        }
        if(id){
            fetchCourseDetails();
        }
    }, [id])

    async function handleEnroll() {
        const res = await createEnrollment({course: course.id});
        console.log(res);
        
        alert("Enrolled Successfully!");
    }

    if(isLoading){
        return <div>Loading...</div>;
    }
    return (
        <div>
            <p>Details of {course?.title}</p>
            <p>{course?.description}</p>
            <p>Teacher: {teacher?.name}, {teacher?.subject}</p>
            <button onClick={handleEnroll}>Enroll Now</button>
        </div>
    )
}

export default CourseDetails;