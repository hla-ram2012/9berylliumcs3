# Computational Thinking Exercise: "Smart School Canteen Queue"
# **Section:** 9-Beryllium
# **Name:** Hugo Lian A. Ramirez
# **Date:** 08/21/26
# **Score:** _____

## Scenario


The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

# Step 1: Identify the Big Problem

**Main Problem:** The PSHS school canteen gets severely crowded during the lunch break because of the food-buying process being too slow and inefficient.

# Step 2: Identify three to four Sub-Problems

1. Scholars spend too much time making decisions on what they will order at the counter.
2. The cashier takes a long time calculating totals and counting change.
3. There is no system to monitor food stock and alerting the staff when items are running out.
4. The layout of the school canteen combined with the unmanaged lines causes overcrowding.

# Step 3: Define Computational Thinking Approaches

For each sub-problem, apply CT skills:

## 1. Ordering Delays

**CT Skill:** Decomposition *(or Abstraction)*

**Example solution:** Create a digital menu board displaying only the food name, the price, and  the current availability so students can decide before reaching the counter.

## 2. Manual Transaction Bottleneck

**CT Skill:** Algorithm Design

**Example solution:** Program a basic system that automatically sums item costs, applies discounts, and calculates exact change instantly, and displays the amount in a digital screen.

## 3. Inventory Tracking Failure

**CT Skill:** Pattern Recognition

**Example solution:** Design an automated database that shows the stock of each item dynamically upon purchase and triggers an alert or a signal when an item is close to running out.

# Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

START
    DISPLAY available_food_items
    total = 0
    FOR EACH item ordered
        ADD item price TO total
    DISPLAY total
    INPUT cash_given
    change = cash_given - total
    DISPLAY change
    GIVE change
    UPDATE available_food_items
END
