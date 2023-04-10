/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2023 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include <stdio.h>
#include <math.h>

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
UART_HandleTypeDef huart1;

/* USER CODE BEGIN PV */

uint8_t UART1_rxBuffer[16]={0};
uint16_t Buffer_position[3];
uint16_t Buffer_orientation[3];

uint8_t flag = 0;
uint16_t Angle1=0;
uint16_t Angle2=0;
uint16_t Angle3=0;
uint16_t Angle4=0;
uint16_t Angle5=0;

//angle de comparaison

uint16_t Angle1comp=0;
uint16_t Angle2comp=0;
uint16_t Angle3comp=0;
uint16_t Angle4comp=0;
uint16_t Angle5comp=0;


/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
	if(huart->Instance==USART1)
	{
		flag = 1;
		HAL_UART_Receive_IT(&huart1, UART1_rxBuffer, 16);
	}
 }

void position2deg(uint16_t Positon[],uint16_t Angle[]){
	uint16_t Px = Positon[0];
	uint16_t Py = Positon[1];
	uint16_t Pz = Positon[2];

	//distance articulation
	uint16_t d1 = 50;
	uint16_t d2 = 300;
	uint16_t d3 = 200;

	//calcul angle1
	Angle1 = atan2(Py,Px);

	//calcul angle2
	uint16_t z1 = cos(Angle1)*Px + sin(Angle1)*Py;
	uint16_t z2 = Pz - d1;
	Angle2 = atan2(sqrt(1.0-(pow((pow(z1,2)+pow(z2,2)-pow(d2,2)-pow(d3,2))/(2*d2*d3),2))),(pow(z1,2)+pow(z2,2)-pow(d2,2)-pow(d3,2))/(2*d2*d3));

	//calcul angle3
	uint16_t b1 = d2+d3*cos(Angle2);
	uint16_t b2 = d3*cosf(Angle2);
	Angle3 = atan2((b1*z2-b2*z1)/(pow(b1,2)+pow(b2,2)),(b1*z1+b2*z2)/(pow(b1,2)+pow(b2,2)));

	//conversion radiant en degres
	Angle1 = Angle1*(180/3.1415926535);
	Angle2 = Angle2*(180/3.1415926535);
	Angle3 = Angle3*(180/3.1415926535);
}

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */
  HAL_UART_Receive_IT(&huart1, UART1_rxBuffer, 16);

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	  if(flag){
		  HAL_UART_Transmit(&huart1, UART1_rxBuffer,16, 100);

		  if((UART1_rxBuffer[0]&&UART1_rxBuffer[15]== 255))
		  {
			  Buffer_position[0] = (UART1_rxBuffer[2]<<8)+ UART1_rxBuffer[3];
			  Buffer_position[1] = (UART1_rxBuffer[4]<<8)+ UART1_rxBuffer[5];
			  Buffer_position[2] = (UART1_rxBuffer[6]<<8)+ UART1_rxBuffer[7];

			  Buffer_orientation[0] = (UART1_rxBuffer[8]<<8)+ UART1_rxBuffer[9];
			  Buffer_orientation[0] = (UART1_rxBuffer[10]<<8)+ UART1_rxBuffer[11];
			  Buffer_orientation[0] = (UART1_rxBuffer[12]<<8)+ UART1_rxBuffer[13];

			  position2deg(Buffer_position,Buffer_orientation);

			  //pour evité de bouger un moteur qui est deja à la bonne position
			  if(Angle1 != Angle1comp){
				  Angle1 = Angle1comp;
				  //on bouge le moteur1
			  }
			  else if(Angle2 != Angle2comp){
				  Angle2 = Angle2comp;
				  //on bouge le moteur2
			  }
			  else if(Angle2 != Angle2comp){
				  Angle2 = Angle2comp;
				  //on bouge le moteur3
			  }
			  else if(Angle3 != Angle3comp){
				  Angle3 = Angle3comp;
				  //on bouge le moteur4
			  }
			  else if(Angle4 != Angle4comp){
				  Angle4 = Angle4comp;
				  //on bouge le moteur5
			  }
			  else if(Angle5 != Angle5comp){
				  Angle5 = Angle5comp;
				  //on bouge le moteur6
			  }else{}
		  }
		  flag = 0;
	  }

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE2);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_NONE;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 115200;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOA_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
