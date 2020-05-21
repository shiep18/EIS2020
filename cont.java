package com.example.myapplication;

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

public class cont extends AppCompatActivity {
    private TextView textView3;
    private Button button,back;
    boolean flag = false;
    int time_a = 0;
    Handler handler = new Handler(){
        public void handleMessage(Message msg){
            if (msg.what == 0x01){
                textView3.setText("计时器："+msg.obj.toString());
                Toast.makeText(cont.this,"计时器："+msg.obj.toString(),Toast.LENGTH_SHORT).show();
            }

            if(msg.what == 0x02){
                textView3.setText("22222222");
            }
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_cont);
        flag = true;
        textView3 = findViewById(R.id.textView3);
        button = findViewById(R.id.button);
        back = findViewById(R.id.button6);
        new Thread(){
            public void run(){
                while (flag){
                    time_a = time_a + 1;
                    SimpleDateFormat format =new SimpleDateFormat("yyyy年mm月dd HH:mm:ss");
                    String timeStr = format.format(System.currentTimeMillis());
                    Message msg = new Message();
                    msg.what = 0x01;
                    msg.obj = time_a;
                    handler.sendMessage(msg);
                    try{
                        Thread.sleep(2000);
                    }catch (InterruptedException e){
                        e.printStackTrace();
                    }
                }
            }
        }.start();
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (flag == false)
                {

                    flag = true;
                }
                else flag=false;
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(cont.this,Main2Activity.class);
                startActivity(intent);
            }
        });
    }
}