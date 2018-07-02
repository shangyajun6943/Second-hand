var $input_uername=$("input[name='username']");
var $input_password=$("input[type='password']");

$input_uername.blur(function(){
    var str=$(this).val();
    var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('Username:×(首字母必须字母,6-20长度)').css({"color":"red"});
        }else{
        $(this).prev().html('Username:√').css({"color":"green"})
        }
    });
$input_password.blur(function(){
    var str=$(this).val();
    var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('Password:×(首字母必须字母,6-20长度)').css({"color":"red"});
        }else{
        $(this).prev().html('Password:√').css({"color":"green"})
        }
    });