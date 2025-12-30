#!/usr/bin/env python3
"""
Simple Calculator CLI App
Supports basic arithmetic, scientific functions, history, and unit conversions.
"""

import math
import os
from typing import List, Tuple

class Calculator:
    def __init__(self):
        self.history: List[Tuple[str, float]] = []
    
    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append((f"{a} + {b}", result))
        return result
    
    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self.history.append((f"{a} - {b}", result))
        return result
    
    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self.history.append((f"{a} × {b}", result))
        return result
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append((f"{a} ÷ {b}", result))
        return result
    
    def power(self, a: float, b: float) -> float:
        result = math.pow(a, b)
        self.history.append((f"{a} ^ {b}", result))
        return result
    
    def sqrt(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(a)
        self.history.append((f"√{a}", result))
        return result
    
    def sin(self, a: float) -> float:
        result = math.sin(math.radians(a))
        self.history.append((f"sin({a}°)", result))
        return result
    
    def show_history(self) -> None:
        if not self.history:
            print("No calculations yet!")
            return
        print("\n📋 Calculation History:")
        print("-" * 40)
        for i, (expr, res) in enumerate(self.history[-10:], 1):  # Last 10
            print(f"{i:2d}. {expr} = {res:.4f}")
        print("-" * 40)
    
    def clear_history(self) -> None:
        self.history.clear()
        print("✅ History cleared!")

def main():
    calc = Calculator()
    print("🧮 Simple Calculator")
    print("Enter 'quit' to exit, 'history' for history, 'clear' to clear history")
    print("Supports: +, -, ×, ÷, ^, √, sin(degrees)")
    
    while True:
        try:
            expr = input("\n➤ ").strip()
            
            if expr.lower() in ['quit', 'exit', 'q']:
                print("👋 Thanks for using Simple Calculator!")
                break
            
            if expr.lower() == 'history':
                calc.show_history()
                continue
            
            if expr.lower() == 'clear':
                calc.clear_history()
                continue
            
            if expr.startswith('√'):
                num = float(expr[1:])
                result = calc.sqrt(num)
                print(f"✅ √{num} = {result:.4f}")
            
            elif expr.startswith('sin('):
                num = float(expr[4:-1])
                result = calc.sin(num)
                print(f"✅ sin({num}°) = {result:.4f}")
            
            else:
                # Parse basic operations
                parts = expr.replace('×', '*').replace('÷', '/').split()
                if len(parts) == 3:
                    a, op, b = parts
                    a, b = float(a), float(b)
                    
                    if op == '+': result = calc.add(a, b)
                    elif op == '-': result = calc.subtract(a, b)
                    elif op == '*': result = calc.multiply(a, b)
                    elif op == '/': result = calc.divide(a, b)
                    elif op == '^': result = calc.power(a, b)
                    else: raise ValueError(f"Unknown operator: {op}")
                    
                    print(f"✅ {a} {op} {b} = {result:.4f}")
                else:
                    print("❌ Format: '5 + 3' or '√16' or 'sin(30)'")
                    
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
