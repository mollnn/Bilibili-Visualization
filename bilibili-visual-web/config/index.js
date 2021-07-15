module.exports={
    devServer:{
        proxy:{
            ["/api"]:{
            target:'http://131.mollnn.com:5000',
              changeOrigin:true,
                pathRewrite: {
                    ['^' + "/api"]: ''
                }
            }
        }

    }
}