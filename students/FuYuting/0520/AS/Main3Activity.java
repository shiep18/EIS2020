package com.example.anew;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;

public class Main3Activity extends AppCompatActivity {
    private TextView textView3;
    private Button button4,button5;
    boolean flag =false;
    int time_a=0;
    Handler handler =new Handler(){
        public  void  handleMessage(Message msg){
            if(msg.what == 0x01){
                textView3.setText("计时器："+msg.obj.toString());
                Toast.makeText(Main3Activity.this, "计时器"+msg.obj.toString(), Toast.LENGTH_SHORT).show();
            }
            if (msg.what ==0x02){
                textView3.setText("22222222");
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        flag =true;
        textView3=findViewById(R.id.textView3);
        button4=findViewById(R.id.button4);
        button5=findViewById(R.id.button5);
        new Thread(){
            public void  run(){
                while (flag){
                    time_a=time_a+1;
                    SimpleDateFormat format =new SimpleDateFormat("yyyy年MM月dd HH:mm:ss");
                    String timeStr =format.format(System.currentTimeMillis());
                    Message msg =new Message();
                    msg.what=0x01;
                    msg.obj=timeStr;  //计时器
                    //msg.obj=time_a;  //现在日期时间
                    handler.sendMessage(msg);
                    try{
                        Thread.sleep(1000);    //2000ms:同步、1000：不会
                    } catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }.start();
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag=false;
            }
        });
        button5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_xian= new Intent(Main3Activity.this,MainActivity.class);
                startActivity(intent_xian);
            }
        });
    }
}
