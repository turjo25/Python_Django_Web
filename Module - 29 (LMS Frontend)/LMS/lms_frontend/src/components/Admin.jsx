import { createCourse } from "../services/courseService";
import { createTeacher } from "../services/teacherService";
import { createStudent } from "../services/studentService";
import { createEnrollment } from "../services/enrollmentService";

function Admin() {
    async function handleCourseCreate(event) {
        event.preventDefault();

        const values = {
            title: event.target.title.value,
            description: event.target.description.value,
            teacher: event.target.teacher.value,
        }
        await createCourse(values);
    }
    async function handleTeacherCreate(event) {
        event.preventDefault();

        const values = {
            name: event.target.name.value,
            subject: event.target.subject.value,
        }
        await createTeacher(values);
    }
    async function handleStudentCreate(event) {
        event.preventDefault();

        const values = {
            name: event.target.name.value,
            enrollment_date: event.target.enrollment_date.value,
        }
        await createStudent(values);
    }

    async function handleEnrollmentCreate(event) {
        event.preventDefault();

        const values = {
            student: event.target.student.value,
            course: event.target.course.value,
        }
        await createEnrollment(values);
    }
    return (<div className="w-full min-h-screen">
        <section className="my-12 px-8">
            <h1 className="text-2xl font-bold mb-6">Teacher Management</h1>
            <div>
                <form onSubmit={handleTeacherCreate} className="flex flex-col gap-4 mb-6">
                    <input name="name" type="text" placeholder="Enter Teacher Name" className="p-2 border border-gray-300 rounded-md"/>
                    <input name="subject" type="text" placeholder="Enter Subject" className="p-2 border border-gray-300 rounded-md"/>
                    <button type="submit" className="bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700">Add Teacher</button>
                </form>
            </div>
            <hr/>
        </section>
        <section className="my-12 px-8">
            <h1 className="text-2xl font-bold mb-6">Course Management</h1>
            <div>
                <form onSubmit={handleCourseCreate} className="flex flex-col gap-4 mb-6">
                    <input name="title" type="text" placeholder="Enter Course Title" className="p-2 border border-gray-300 rounded-md"/>
                    <input name="description" type="text" placeholder="Enter Course Description" className="p-2 border border-gray-300 rounded-md"/>
                    <input name="teacher" type="text" placeholder="Enter Teacher Id" className="p-2 border border-gray-300 rounded-md"/>
                    <button type="submit" className="bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700">Add Course</button>
                </form>
            </div>
            <hr/>
        </section>
        <section className="my-12 px-8">
            <h1 className="text-2xl font-bold mb-6">Student Management</h1>
            <div>
                <form onSubmit={handleStudentCreate} className="flex flex-col gap-4 mb-6">
                    <input name="name" type="text" placeholder="Enter Student Name" className="p-2 border border-gray-300 rounded-md"/>
                    <input name="enrollment_date" type="date" placeholder="Enter Enrollment Date" className="p-2 border border-gray-300 rounded-md"/>
                    <button type="submit" className="bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700">Add Student</button>
                </form>
            </div>
            <hr/>
        </section>
        <section className="my-12 px-8">
            <h1 className="text-2xl font-bold mb-6">Enrollment Management</h1>
            <div>
                <form onSubmit={handleEnrollmentCreate} className="flex flex-col gap-4 mb-6">
                    <input name="student" type="text" placeholder="Enter Student ID" className="p-2 border border-gray-300 rounded-md"/>
                    <input name="course" type="text" placeholder="Enter Course ID" className="p-2 border border-gray-300 rounded-md"/>
                    <button type="submit" className="bg-blue-600 text-white p-2 rounded-md cursor-pointer hover:bg-blue-700">Add Enrollment</button>
                </form>
            </div>
            <hr/>
        </section>
    </div>)
}

export default Admin;