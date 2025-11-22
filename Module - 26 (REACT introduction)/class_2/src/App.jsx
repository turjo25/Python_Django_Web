import './App.css'
import Course from './Course'
import CourseCard from '../CourseCard.jsx'

function App() {

  //---Function for event listener:------
  function handleForm() {
      event.preventDefault();
      
      //array diye
      // alert('Form submitted with username: ' + event.target[0].value + ' and email: ' + event.target[1].value);

      //name diye
      alert('Form submitted with username: ' + event.target.username.value + ' and email: ' + event.target.email.value);
    }

  // ------if else evabe likha jabe------
  // const isUserLoggedIn = false;
  // if (isUserLoggedIn)
  //   return <Course/>
  // else
  //   return <div>Please log in to continue</div>


  //-------switch case:-----------------
  // const number = 10;
  // switch(number){
  //   case 1:
  //     return <div>Number is One</div>
  //   case 5:
  //     return <div>Number is Five</div>
  //   case 10:
  //     return (
  //       <>
  //         <h1>Number is Ten</h1>
  //         <Course/>
  //       </>
  //     )
  //   default:
  //     return <div>Number is not found</div>
  // }

  //-------Operator:--------------------
  // and operator (&&)
  // or operator (||)
  // not equal operator (!=) 
  // three equal operator (===) (value and type both check)
  // const age = 20;
  // const gender = 'F';
  // return(
  //   <>
  //   <div>Welcome to React Class</div>
  //   {age >=18 && gender ==='M' ? <Course/> : <div>Access Denied</div>}
  //   </>
  // )


  //--------Immediatly invoked function:----------------
  const age = 20;
  const gender = 'M';
  const courses = ['React', 'JavaScript', 'HTML'];
  return(
    <>
    <div>Welcome to React Class</div>
    {(function(){
      if(age >=18 && gender ==='M'){
        return (
          <div>
            <h2>Available Courses:</h2>
              {courses.map((course) => (
                <CourseCard name={course}/>
              ))}
          </div>
        )
      }else{
        return <div>Access Denied</div>
      }
    })()}
    
    <form action="#" className='flex flex-col w-1/3 m-4 p-4 border' onSubmit={handleForm}>
      <input name='username' type="text" placeholder="Enter your name" className='border p-2 m-2' required/>
      <input name='email' type="email" placeholder="Enter your email" className='border p-2 m-2' required/>
      <button type="submit" className='border p-2 m-2 bg-blue-500 text-white'>Submit</button>
    </form>
    </>
  )

  return (
    <></>
  )
}

export default App
