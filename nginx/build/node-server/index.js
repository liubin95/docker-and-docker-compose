const express = require('express')
const moment = require('moment');
// const cors = require('cors');
const app = express()

// app.use(cors())
app.get('/api/date', function (req, res) {
    res.send(moment().format("YYYY-MM-DD HH:mm:ss"));
})

app.listen(3000, () => {
    console.log(`alive at ${moment().format("YYYY-MM-DD HH:mm:ss")}`)
})