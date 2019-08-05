require(requirejs);
const translate = require('translate-api');
 
let transUrl = 'https://nodejs.org/en/';
translate.getPage(transUrl).then(function(htmlStr){
  console.log(htmlStr.length)
});

let transText = 'hello world!';
translate.getText(transText,{to: 'zh-CN'}).then(function(text){
  console.log(text)
});