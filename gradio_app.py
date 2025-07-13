def run_automl(file, target):
    df = pd.read_csv(file.name)
    X, y = prepare_data(file.name, target)

    best_model_name, best_model = select_best_model(X, y)

    # ✅ FIXED: Add stratify for better label distribution
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
    except ValueError:
        print("⚠️ Warning: Could not stratify due to small class sizes. Falling back to normal split.")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    best_model.fit(X_train, y_train)

    # Plot evaluation and save to file
    plt.clf()
    evaluate_model(best_model, X_test, y_test)
    plot_path = "output_plot.png"
    plt.savefig(plot_path)

    return f"Best Model: {best_model_name}", plot_path
