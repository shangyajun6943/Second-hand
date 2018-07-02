var $input_uername=$("input[name='username']");
var $input_password1=$("input[name='password1']");

var $input_password2=$("input[name='password2']");

var $input_tel=$("input[name='tel']");
var $input_post_code=$("input[name='post_code']");
var $input_email=$("input[name='email']");
// 用户名格式验证
$input_uername.blur(function(){
    var str=$(this).val();
    var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('Username:×(首字母必须字母,6-20长度)').css({"color":"red"});
        }else{
        $(this).prev().html('Username:√').css({"color":"green"})
        result=userver(str)
            if(result==='1'){
                $(this).focus().prev().html('Username:已存在').css({"color":"red"});
            }
        }
    });
var userver=function(username){
    url1="/account/Verifyum?username="+username;
    var $rs=0;
    $.ajax({
        type:"get",
        url:url1,
        async:false,
        success : function(result) {
            $rs=result
        }
    });
    return $rs;
};
$input_password1.blur(function(){
    var str=$(this).val();
    var ret=/^[a-zA-Z][a-zA-Z0-9_]{5,20}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('Password:×(首字母必须字母,6-20长度)').css({"color":"red"});
        }else{
        $(this).prev().html('Password:√').css({"color":"green"})
        }
    });

// 本来想实现密码1跟密码2不同清空两个input且焦点回到密码1，结果chrome上不行火狐可以
$input_password2.blur(function(){
    var str=$(this).val();
    var ret=$input_password1.val();
    if(str!==ret){
        $(this).prev().html('Password:×(两次密码不一致)').css({"color":"red"});
        $input_password2.val('');
    }
    else if(str!==''){
        $(this).prev().html('Password:√').css({"color":"green"})
        }
    });


$input_email.blur(function(){
    var str=$(this).val();
    var ret=/^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('email:×(必须符合***@***.com的格式)').css({"color":"red"});
    }
    else{
        $(this).prev().html('email:√').css({"color":"green"})
        }
});

$input_tel.blur(function(){
    var str=$(this).val();
    var ret=/^13[1-9]\d{8}|15[1-9]\d{8}|18[1-9]\d{8}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('tel:×(必须符合手机号码的格式)').css({"color":"red"});
    }
    else{
        $(this).prev().html('tel:√').css({"color":"green"})
        }
});

$input_post_code.blur(function(){
    var str=$(this).val();
    var ret=/^\d{6}$/;
    if(!ret.test(str)){
        $(this).focus().prev().html('post_code:×(必须符合邮政编码的格式)').css({"color":"red"});
    }
    else{
        $(this).prev().html('post_code:√').css({"color":"green"})
        }
});



