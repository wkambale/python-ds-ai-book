# Use a colorblind-friendly palette
sns.set_palette('colorblind')

# Or specify viridis for sequential data
plt.figure()
sns.barplot(data=df_clean.reset_index(), x='transaction_type', y='amount', palette='viridis')
plt.title('Colorblind-Friendly Visualization')
plt.show()