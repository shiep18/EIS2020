package com.example.new_test4;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private EditText userName;
    private TextView passWord;
    private Button login, cancel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        userName = findViewById(R.id.username);
        passWord = findViewById(R.id.password);
        login = findViewById(R.id.btn_login);
        cancel = findViewById(R.id.btn_cancel);
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, Main2Activity.class);
                String username_0 = new String("test");
                String password_0 = new String("password123");
                if (username_0.equals(userName.getText().toString()) && password_0.equals(passWord.getText().toString())){
                    intent.putExtra("userName", userName.getText().toString());
                    intent.putExtra("password", passWord.getText().toString());
                    startActivity(intent);
                }
                else {
                    Toast.makeText(MainActivity.this, "error", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}

