# Personal Protective Equipment (PPE) Detection

## Introduction

Accidents in construction sites often result from the lack of proper safety equipment for workers. To enhance safety and compliance, we have trained a model capable of detecting Personal Protective Equipment (PPE) on workers, aligning with OSHA standards. This model can be further integrated for tracking, safety monitoring, and triggering alarms in real-world scenarios.

This project utilizes a pretrained model from [this repository] and applies **transfer learning** to fine-tune it for additional classes, enabling detection of more comprehensive safety attributes.

## Dataset

The dataset used for training and validation includes labeled images in YOLOv8 format. It consists of **7057 image samples** split into the following subsets:  
- **Training set**: 6402 samples  
- **Validation set**: 321 samples  
- **Test set**: 334 samples  

The dataset has been expanded to include 16 classes, as listed below:  
1. **Hardhat**  
2. **Mask**  
3. **NO-Hardhat**  
4. **NO-Mask**  
5. **NO-Safety Vest**  
6. **Person**  
7. **Safety Cone**  
8. **Safety Vest**  
9. **Machinery**  
10. **Vehicle**  
11. **Gloves**  
12. **NO-Gloves**  
13. **Glasses**  
14. **NO-Glasses**  
15. **Safety Shoes**  
16. **NO-Safety Shoes**  

## Transfer Learning Approach

We employed **transfer learning** to adapt the existing pretrained model to detect additional classes. This approach helped us to significantly reduce training time while leveraging the robustness of the pretrained model. The fine-tuning process involved:  
- Incorporating the expanded dataset with the additional PPE classes.  
- Optimizing the model to ensure alignment with OSHA safety standards.  

## Applications

This model can be utilized in various safety monitoring applications, such as:  
- Construction site surveillance for PPE compliance.  
- Real-time alarm triggering in case of missing PPE.  
- Worker tracking to improve overall safety and productivity.  

For further details or inquiries, please reach out.