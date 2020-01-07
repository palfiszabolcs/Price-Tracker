package com.example.pricetracker.Database;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.RecyclerView;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.pricetracker.R;

public class FirebaseViewHolder extends RecyclerView.ViewHolder {


    public ImageView image;
    public TextView name;
    public TextView price;
    public TextView currency;
    public TextView category;
    public CardView card;

    public FirebaseViewHolder(@NonNull View itemView) {
        super(itemView);
        image = itemView.findViewById(R.id.productImage);
        name = itemView.findViewById(R.id.productName);
        category = itemView.findViewById(R.id.productType);
        price = itemView.findViewById(R.id.price);
        currency = itemView.findViewById(R.id.currency);
        card = itemView.findViewById(R.id.cardView);
        //card.setBackgroundColor(Color.TRANSPARENT);
        card.getBackground().setAlpha(128);
        //card.setCardElevation(0);
    }
}
