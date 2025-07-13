import typer
from eduautoml.model_selection import select_best_model
from eduautoml.evaluation import evaluate_model
from eduautoml.preprocessing import prepare_data
from sklearn.model_selection import train_test_split

app = typer.Typer()

@app.command()
def run(input: str, target: str):
    typer.echo(f"Running AutoML on {input} with target column {target}")

    # ✅ Use the real preprocessing
    X, y = prepare_data(input, target)

    best_model_name, best_model = select_best_model(X, y)
    typer.echo(f"Best model: {best_model_name}")

    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
    except ValueError:
        typer.echo("⚠️ Stratified split failed. Falling back to random split.")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    best_model.fit(X_train, y_train)
    evaluate_model(best_model, X_test, y_test)

if __name__ == "__main__":
    app()
