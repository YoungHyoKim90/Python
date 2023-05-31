package kr.co.aiai.app;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity8 extends AppCompatActivity {

    private TextView tvFirst;
    private TextView tvLast;
    private EditText etFirst;
    private EditText etLast;
    private Button btn;
    private TextView tv1;

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main8);

            tvFirst = findViewById(R.id.tvFirst);
            tvLast = findViewById(R.id.tvLast);
            etFirst = findViewById(R.id.etFirst);
            etLast = findViewById(R.id.etLast);
            btn = findViewById(R.id.btn);
            tv1 = findViewById(R.id.tv1);

            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    int startNumber = Integer.parseInt(etFirst.getText().toString());
                    int endNumber = Integer.parseInt(etLast.getText().toString());
                    StringBuilder output = new StringBuilder();

                    for (int i = startNumber; i <= endNumber; i++) {
                        output.append("\n");
                        for(int j=startNumber;j<i;j++){
                            output.append("*");
                        }
                    }

                    tv1.setText(output.toString());
                }
            });
        }
    }


