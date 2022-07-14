package com.ctf101.pact04;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.nio.charset.StandardCharsets;

public class MainActivity extends AppCompatActivity {
    private TextView secret;
    private Button connect;
    private EditText password;

    private static final byte[] xorxor = {0x37, 0x0e, 0x1c, 0x07, 0x0a, 0x25, 0x16, 0x23, 0x09, 0x0f, 0x2c, 0x34, 0x00, 0x24, 0x06, 0x36, 0x2b, 0x00, 0x2d, 0x3d, 0x1b, 0x20, 0x50};
    private static final byte[] encoded = {0x16,0x13,0x13,0x1f,0x04,0x6c,0x44,0x70,0x18,0x00,0x53,0x32,0x0a,0x24,0x0d,0x49,0x31,0x04,0x1e,0x0c,0x30,0x17,0x1d,0x74,0x00,0x04,0x0c,0x08,0x6c,0x09,0x35,0x4c,0x13,0x1f,0x23,0x08,0x71,0x36,0x3d,0x01,0x54,0x42,0x54,0x2f,0x4b,0x0e,0x60,0x02,0x14,0x08,0x58,0x79,0x00,0x35,0x5e,0x16,0x10,0x7b,0x0c,0x62,0x42,0x59,0x76,0x5c,0x47,0x00,0x66,0x11,0x0a,0x67,0x02,0x17,0x0f,0x59,0x7e,0x53,0x2d};

    private byte[] XOR(byte[] a, byte[] b) {

        byte[] result = a.clone();
        for(int i=0; i < a.length; i++) {
            result[i] = (byte)(a[i] ^ b[i%b.length]);
        }
        return result;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        secret = (TextView) findViewById(R.id.secret);
        password = (EditText) findViewById(R.id.password_input);
        connect = (Button) findViewById(R.id.connect);
        secret.setVisibility(View.INVISIBLE);

        connect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String input = password.getText().toString();
                if(input.length() == 0) {
                    Toast.makeText(MainActivity.this, "T'as vraiment cru que je ne mettrai pas de mot de passe ?", Toast.LENGTH_LONG).show();
                    return;
                }
                String input_xored = new String(XOR(input.getBytes(StandardCharsets.UTF_8), xorxor), StandardCharsets.UTF_8);
                secret.setText(new String(XOR(encoded, input.getBytes(StandardCharsets.UTF_8))));
                if(!input_xored.contentEquals("connaissez_vous_le_XOR?")) {
                    Toast.makeText(MainActivity.this, "Bah alors ? On s'est trompé ?", Toast.LENGTH_LONG).show();
                }

                secret.setVisibility(View.VISIBLE);
            }
        });
    }
}