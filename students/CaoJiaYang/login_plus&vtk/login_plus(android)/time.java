package com.example.two;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.view.View;
import android.widget.Button;
import android.widget.SimpleAdapter;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;

public class time extends AppCompatActivity {
    private TextView textView;
    private Button button;
    int time_a=0;
    boolean flag=false;
    Handler handler=new Handler(){
        public void handleMessage(Message msg){
            if (msg.what==0x01){
                textView.setText("计时器："+msg.obj.toString());
                Toast.makeText(time.this,"计时器："+msg.obj.toString(),Toast.LENGTH_SHORT).show();
            }
            if (msg.what==0x002){
                textView.setText("22222222");
            }
        }
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_time);
        flag=true;
        textView=findViewById(R.id.textView);
        button=findViewById(R.id.button);
        new Thread(){
            public void run(){
                while (flag){
                    time_a=time_a+1;
                    SimpleDateFormat format=new SimpleDateFormat("yyyy年MM月dd日 HH:mm:ss");
                    String timeStr=format.format(System.currentTimeMillis());
                    Message msg=new Message();
                    msg.what=0x01;
                    msg.obj=timeStr;
                    //msg.obj=time_a;
                    handler.sendMessage(msg);
                    try{
                        Thread.sleep(1000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }.start();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag=false;
            }
        });

    }
}
