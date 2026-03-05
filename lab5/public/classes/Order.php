<?php
class Order {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    #region CRUD:
    public function create($name, $email, $model, $amount, $assembly_included, $delivery) {
        $stmt = $this->pdo->prepare(
            "INSERT INTO orders (name, email, model, amount, assembly_included, delivery) VALUES (?, ?, ?, ?, ?, ?)"
        );
        $stmt->execute([$name, $age, $faculty, $agree_rules, $study_form]);
    }

    public function readAll() {
        $stmt = $this->pdo->query("SELECT * FROM students");
        return $stmt->fetchAll();
    }

    public function update($id, $name) {
        $stmt = $this->pdo->prepare("UPDATE students SET name=? WHERE id=?");
        $stmt->execute([$name, $id]);
    }

    public function delete($id) {
        $stmt = $this->pdo->prepare("DELETE FROM students WHERE id=?");
        $stmt->execute([$id]);
    }
    #endregion
}