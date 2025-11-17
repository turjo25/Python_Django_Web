function New(){
    const project = ['Project A','Project B','Project C']
    return(
        <div>
            {
                project.map((project,index)=>{
                    return <div key={index}>{project}</div>
                })
            }
        </div>
    )
}
export default New