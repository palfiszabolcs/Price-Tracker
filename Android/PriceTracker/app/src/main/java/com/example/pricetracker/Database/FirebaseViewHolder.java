package com.example.pricetracker.Database;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.pricetracker.R;

public class FirebaseViewHolder extends RecyclerView.ViewHolder {


    public ImageView productImage;
    public TextView productName;
    public TextView productDescription;
    public TextView productPrice;
    public TextView productType;

    public FirebaseViewHolder(@NonNull View itemView) {
        super(itemView);
        productImage = itemView.findViewById(R.id.productImage);
        productName = itemView.findViewById(R.id.productName);
        productDescription = itemView.findViewById(R.id.productDescription);
        productPrice = itemView.findViewById(R.id.productPrice);
        productType = itemView.findViewById(R.id.productType);
    }
}
