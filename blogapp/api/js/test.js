import axios from 'axios'

axios({
    method: 'get',
    url: 'http://localhost:8000/api/categories',
    headers:{
        Authorization:'Token 815ae0f20ec0e814d6e4df9629fc99a7ec3ea132'
    }
  })
    .then(function (response) {
        console.log(response)
});