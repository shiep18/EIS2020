package com.example.myvideo;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class Main3Activity extends AppCompatActivity {
    private TextView Info;
    private Button media, timer, back;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        Info = findViewById(R.id.textView3);
        media = findViewById(R.id.Media);
        timer = findViewById(R.id.Timer);
        back = findViewById(R.id.Back);

        media.setOnClickListener(new View.OnClickListener() {
            Intent intent_media = new Intent(Main3Activity.this, MainActivity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_media);
            }
        });
        timer.setOnClickListener(new View.OnClickListener() {
            Intent intent_timer = new Intent(Main3Activity.this, Main4Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_timer);
            }
        });
        back.setOnClickListener(new View.OnClickListener() {
            Intent intent_back = new Intent(Main3Activity.this, Main2Activity.class);
            @Override
            public void onClick(View v) {
                startActivity(intent_back);
            }
        });

    }
}
