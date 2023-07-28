# Freelancer BID Server

This applications will bind for project requests and aceept everyone, if one of then gets accepted, send back to user as message
How filenames should be generated?
- MD5 (whatsapp number + first name + surname)
- File contents should be like this:

{
    "firstname" : "John",
    "surname" : "Doe",
    "text" : {
        "selfname" : "Hi, my name is"
        "introduction" : "and i'm a experienced {programmer|software developer|software engineer} and i have experience with {web programming|application development|something} since",
        "working_since" : "2015"
    },
    "settings" : {
        "max_bind_week" : "3",
        "counter" : "0"
    }
}

https://developers.freelancer.com/docs/authentication/creating-a-client
https://github.com/freelancer/freelancer-sdk-python
https://accounts.freelancer.com/settings/develop
https://jsonformatter.curiousconcept.com/#
https://gchq.github.io/CyberChef/#recipe=MD5()&input=OTI1NDI4MDIzSOliZXJK%2Bmxpbw
https://www.geeksforgeeks.org/building-whatsapp-bot-on-python/