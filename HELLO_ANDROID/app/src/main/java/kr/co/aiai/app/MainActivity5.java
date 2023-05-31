package kr.co.aiai.app;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity5 extends AppCompatActivity {

    private EditText et;
    private EditText tv2;
    private Button btn ;

    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main5);

        EditText et = findViewById(R.id.tv);
        TextView tv2 = findViewById(R.id.tv2);
        Button btn = findViewById(R.id.btn1);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View vt2) {
                String inputStr = et.getText().toString();

                int inputNum = Integer.parseInt(inputStr);

                StringBuilder sb = new StringBuilder();

                for(int i =1; i <=9 ; i++) {
                    int result = inputNum *i;
                    sb.append(inputNum).append(" X ").append(i).append(" = ").append(result).append("\n");

                }
                tv2.setText(sb.toString());
            }
        });
    }
}

