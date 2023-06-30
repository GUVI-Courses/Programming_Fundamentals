show dbs
use company

-- insert

db.employee.insertOne({
    name:"Anees",
    role:"Developer",
    salary:50000
})

db.employee.insertMany([
    {
    name:"Arfa",
    role:"Backend developer",
    salary:150000,
    skills:["python","java"]
},

{
    name:"Chandan",
    role:"frontend developer",
    salary:250000,
    skills:["html","css"],
    address:{
        "address1":"chennai",
        "address2":"bangalore"
    }

}

])

-- fetch

db.employee.find().pretty()

-- update

db.employee.updateMany(
    {},
    {$set:{country:"India"}}

)

-- delete

db.employee.deleteOne({_id:ObjectId("64781bc6037e92f8f4787df3")})