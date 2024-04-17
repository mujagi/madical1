//1. ajax stu_score.json 데이터를출력하시오 0
//2. 학생입력 -> 학생추가 프로그램을 구성하시오. 0
//3. 학생수정 -> 학생성적 수정이 가능하게 구성하시오. 
//4. 학생삭제 -> 선택된 학생이 삭제 되도록 구성하시오.
$(function(){
    let s_cont = 0 ;


    //최초 데이터 불러오기
    $.ajax({
        url:"http://127.0.0.1:5500/students/json/stu_score.json",
        data:{},
        type:"get",
        dataType:"json",
        success:function(data){
            //alert("성공");
            let h_data = "";
            
            for(let i = 0;i<10;i++){
                h_data+="<tr>";
                h_data+="<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
                h_data+="<td>"+(s_cont+=1)+"</td>";
                h_data+="<td>"+data[i].name+"</td>";
                h_data+="<td>"+data[i].kor+"</td>";
                h_data+="<td>"+data[i].eng+"</td>";
                h_data+="<td>"+data[i].math+"</td>";
                h_data+="<td>"+data[i].total+"</td>";
                h_data+="<td>"+data[i].avg+"</td>";
                h_data+="<td>"+data[i].rank+"</td>";
                h_data+="<td><button class='delBtn'>삭제</button></td>";
                h_data+="</tr>";         
            }//stu_score.json 불러오기
            $("#body").html(h_data); // 불러온거 tbody에  추가
        },//최초 데이터 불러오기 성공
        error:function(){
            alert("실패");
        } //최초 데이터 불러오기 실패
    }); //최초 데이터 불러오기 

    //학생입력 추가
    $("#writeBtn").click(function(){
        //alert("test");
        $(".p_all").css("display","block");
    });//학생입력 버튼 클릭 시
    $("#confirmBtn").click(function(){   
        $(".p_all").css("display","none");
        $(".p_main h2").text("학생성적입력");
        if($("#name").val() !=""){
            s_cont+=1 ;
            let i_name = $("#name").val();
            let i_kor = Number($("#kor").val());
            let i_eng = Number($("#eng").val());
            let i_math = Number($("#math").val());
            let i_total = i_kor+i_eng+i_math;
            let i_avg = i_total/3;
            
            let h_data = "";
            h_data+="<td><input type='checkbox' name='stu' class='stuChk' value=''></td>";
            h_data+="<td>"+s_cont+"</td>";
            h_data+="<td>"+i_name+"</td>";
            h_data+="<td>"+i_kor+"</td>";
            h_data+="<td>"+i_eng+"</td>";
            h_data+="<td>"+i_math+"</td>";
            h_data+="<td>"+i_total+"</td>";
            h_data+="<td>"+i_avg+"</td>";
            h_data+="<td>"+0+"</td>";
            h_data+="<td><button class='delBtn'>삭제</button></td>";
            $("#body").append(h_data);
        }  
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });//학생입력 확인버튼 클릭시

    //학생입력 확인버튼 클릭 후 입력한 학생 추가
    
    //학생입력 취소버튼 클릭시
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    });//학생입력 취소버튼 클릭시

    

    //학생수정버튼 클릭시
    $("#modifyBtn").click(function(){
        //alert("test");
        
        if($(".stuChk:checked").length<1){
            alert("학생을 체크하셔야 합니다!");
            return false;
        }
        else{
            $(".p_all2").css("display","block");
            
            o_id = $(".stuChk:checked").parent();
            console.log("학번 : "+o_id.next().text());
            //학생수정버튼 확인 누를 시
            $("#confirmBtn2").click(function(){
                $(".p_all2").css("display","none");
                $("#name2").val("");
                $("#kor2").val("");
                $("#eng2").val("");
                $("#math2").val(""); 
            }); //학생수정버튼 확인 누를 시
            
            //학생수정버튼 취소 누를 시
            $("#cancelBtn2").click(function(){
                $(".p_all2").css("display","none"); 
                $("#name2").val("");
                $("#kor2").val("");
                $("#eng2").val("");
                $("#math2").val("");  
            });//학생수정버튼 취소 누를 시
        }

    }); //학생수정버튼 클릭시

}); //제이쿼리 선언