$(document).ready(function(){
            for(var i=2011;i<=2015;i++){
                $("#"+i).css({'display':'none'});
            }
            $("#menu-2010").addClass("active");
            $('.nav-pills li').click(function(){
                var idName=$(this).attr('id');
                var splitNum=idName.split('-');
                var num=splitNum[1];
                for(var i=2010;i<=2015;i++){
                    if(i==num){
                        $("#menu-"+i).addClass("active");
                        $("#"+i).css({'display':'block'});
                    }else{
                        $("#menu-"+i).removeClass("active");
                        $("#"+i).css({'display':'none'});
                    }
                }
            });
        });