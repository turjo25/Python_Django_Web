function CourseCard({name}) {
    function handleEnroll(){
        console.log(`Enrolling in ${name} course`);
        alert(`You have enrolled in ${name} course!`);
    }
    return (
        <div className="border p-4 bg-gray-50 rounded-sm my-4 flex justify-between items-center">
            <span>Name: {name} </span>
            <button onClick={handleEnroll} className="bg-red-300 text-black px-4 py-2 rounded">Enroll</button>
        </div>
    )
}

export default CourseCard