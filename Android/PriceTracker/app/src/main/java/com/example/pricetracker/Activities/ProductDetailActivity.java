package com.example.pricetracker.Activities;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.pricetracker.Models.Product;
import com.example.pricetracker.R;
import com.github.mikephil.charting.charts.LineChart;
import com.github.mikephil.charting.data.Entry;
import com.github.mikephil.charting.data.LineData;
import com.github.mikephil.charting.data.LineDataSet;
import com.github.mikephil.charting.interfaces.datasets.ILineDataSet;
import com.github.mikephil.charting.listener.OnChartGestureListener;
import com.github.mikephil.charting.listener.OnChartValueSelectedListener;

import java.util.ArrayList;

public class ProductDetailActivity extends AppCompatActivity{

    private static final String TAG = "ProductDetailActivity";
    private LineChart mChart;
    
    private ImageView productImage;
    private TextView productPrice;
    private TextView productName;
    private TextView productDescription;
    private TextView productType;
    private Button openLinkButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_detail);
        getIds();
        Product product = getIntent().getParcelableExtra("product");
        productName.setText(product.getProductName());
        productDescription.setText(product.getProductDescription());
        productPrice.setText(Double.toString(product.getPrice()));
        //productImage.setImageURI(product.getImageURL());
        //productType.setText(product.getProductType());
        /*openLinkButton.setOnClickListener({
                Toast.makeText(getApplicationContext(), "Open Link button clicked!", Toast.LENGTH_LONG).show();
                Intent openLinkActivity = new Intent(getApplicationContext(), openLinkActivity.class);
                startActivity(openLinkActivity);
        });*/

        //LineChart
        mChart = (LineChart) findViewById(R.id.linechart);

        //mChart.setOnChartGestureListener(ProductDetailActivity.this);
        //mChart.setOnChartValueSelectedListener(ProductDetailActivity.this);

        mChart.setDragEnabled(true);
        mChart.setScaleEnabled(false);

        ArrayList<Entry> yValues = new ArrayList<>();

        yValues.add(new Entry(0, 60f));
        yValues.add(new Entry(1, 50f));
        yValues.add(new Entry(2, 70f));
        yValues.add(new Entry(3, 30f));
        yValues.add(new Entry(4, 50f));
        yValues.add(new Entry(5, 60f));
        yValues.add(new Entry(6, 65f));
        LineDataSet set1 = new LineDataSet(yValues, "Data Set 1");

        set1.setFillAlpha(110);

        //ChartDesign
        //set1.setColor(#24478f);
        set1.setLineWidth(3f);
        set1.setValueTextSize(10f);
        //set1.setValueTextColor(#24478f);

        ArrayList<ILineDataSet> dataSets = new ArrayList<>();
        dataSets.add(set1);

        LineData data = new LineData(dataSets);

        mChart.setData(data);
    }

    @SuppressLint("WrongViewCast")
    public void getIds(){
        productImage = findViewById(R.id.productImage);
        productPrice = findViewById(R.id.productPrice);
        productName = findViewById(R.id.productName);
        productDescription = findViewById(R.id.productDescription);
        productType = findViewById(R.id.productType);
        openLinkButton = findViewById(R.id.openLinkButton);
    }
}
