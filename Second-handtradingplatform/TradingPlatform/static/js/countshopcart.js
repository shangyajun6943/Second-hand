
var count=function(){
    var $shopcart=$(".simpleCart_total");
    $.ajax({
        type:"get",
        url:"/shopcart/countPrice",
        async:true,
        success:function (result) {
            $shopcart.html(result);
        }
    });
};
var $shopcartrm=$(".simpleCart_empty");
$shopcartrm.click(function(){
    remove();
});

var remove=function(){
    $.ajax({
        type:"get",
        url:"/shopcart/removeShopcart",
        async:false,
        success:function (result) {
            window.location.reload()
            console.log("ok");
        }
    });
};
count();