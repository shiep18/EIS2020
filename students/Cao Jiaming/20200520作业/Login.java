package com.example.logintovideo;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class Login extends AppCompatActivity {
    private EditText userName;
    private TextView password;
    private Button login,cancel;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        userName=findViewById(R.id.userName);
        password=findViewById(R.id.password);
        login=findViewById(R.id.login);
        cancel=findViewById(R.id.cancel);
        login.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(Login.this, Select.class);
                String username_0 = new String( "test");
                String password_0 = new String( "password123");
                if (username_0.equals(userName.getText().toString())&&password_0.equals(password.getText().toString())){
                    intent.putExtra("userName",userName.getText().toString());
                    intent.putExtra("password",password.getText().toString());

                    startActivity(intent);
                }
                else{
                    Toast.makeText(Login.this,"账号密码错误",Toast.LENGTH_SHORT).show();
                }

            }
        });
    }
}
