	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;

$("input[name='user_name']").blur(function() {
		check_user_name(this);
		});
	function check_user_name(this1){
			var len = $(this1).val().length;
			if(len<5||len>20)
			{
				$(this1).next().html('请输入5-20个字符的用户名')
				$(this1).next().show();
				error_name = true;
			}
			else
			{
				$(this1).next().hide();
				error_name = false;
			};
	};
		$("input[name='pwd']").blur(function() {
			check_pwd(this);
		});
			function check_pwd(this1){
			var len = $(this1).val().length;
			if(len<8||len>20)
			{
			$(this1).next().html('密码最少8位，最长20位')
			$(this1).next().show();
			error_password = true;
			}
			else
			{
			$(this1).next().hide();
			error_password = false;
			}		
		};




	$('#email').blur(function() {
		check_email();
	});

	$('#allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});
	$("input[name='cpwd']").blur(function() {
		check_cpwd(this);
		});
	function check_cpwd(this1){
		var pass = $("input[name='pwd']").val();
		var cpass = $(this1).val();

		if(pass!=cpass)
		{
			$(this1).next().html('两次输入的密码不一致')
			$(this1).next().show();
			error_check_password = true;
		}
		else
		{
			$(this1).next().hide();
			error_check_password = false;
		};	
		
	};
	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	};


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});