
// 全选框
$('#select_all').click(function(){
    // 获取select_all的checked属性--使用prop，而不是attr，attr会让属性变成undefined类型
    if($(this).prop("checked")){
        // 全选选中时，复选框状态
        $("input[name='select_one']").prop("checked",true);
        console.log(1);
    }else{
        // 全选未选中时，复选框状态
        $("input[name='select_one']").prop("checked",false);
        console.log(0);
    }
});

// 单选框
$("input[name='select_one']").click(function () {
    if($("input[name='select_one']").not("input:checked").size()<=0){
        $('#select_all').attr("checked",true);
    }else{
        $('#select_all').attr("checked",false);
    }
});







// 以下为 未完成功能：物品数量增加减少，点击删除，全选或者单选后价格动态变化。
var $delete = $("a[name='del']");
$delete.click(function () {
    var $id=$(this).attr("ord");
    url1="/shopcart/remove";
    data1={
        "orderid":$id
    };
    remove(url1,data1);
});
var remove=function (url1,data1) {
    $.ajax({
        type:"post",
        url:url1,
        data:data1,
        async:false,
        success:function (result) {
            $(window).attr('location','/shopcart/');
        }
    });
};





var $reduce = $("input[class='reduce']");
var $add = $("input[class='add']");
var $quantity = $("input[name='quantity']");
var $subtotal = $("b[name='subtotal']");

$quantity.blur(function(){
    var $val = $(this).val();
    var $price=$(this).parent().siblings().eq(1).html();
    $(this).parent().siblings().eq(3).html(parseFloat($val)*parseFloat($price));
});

// -
$reduce.click(function () {
    var $val = $(this).next().val();
    var $price=$(this).parent().siblings().eq(1).html();
    if ($val==1) {
        $(this).next().val(1);
        $(this).parent().siblings().eq(3).html(parseFloat($val)*parseFloat($price));
    }else{
        $(this).next().val(parseInt($val)-1);
        $(this).parent().siblings().eq(3).html((parseFloat($val)-1)*parseFloat($price));
    }
    total();
});
// +
$add.click(function () {
    var $price=$(this).parent().siblings().eq(1).html();
    var $val = $(this).prev().val();
    $(this).prev().val(parseInt($val)+1);
    $(this).parent().siblings().eq(3).html((parseFloat($val)+1)*parseFloat($price));
    total();
});
// total
var total=function(){
    var $sum=0;
    var $shopcart_total_1=$(".shopcart_total_1");
    $.each($shopcart_total_1,function(index,value){
        $sum+=parseFloat($(value).html());
    });
    $subtotal.html($sum);
};
total();



var get_reduce=function () {
    url1="/shopcart/get_reduce";
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