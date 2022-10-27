import numpy as np


def conv2d(input_data, filter_data):
    batches, input_height, input_width, _input_depth = input_data.shape
    kernel_height, kernel_width, input_depth, output_depth = filter_data.shape
    assert input_depth == _input_depth

    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1

    output = np.zeros(shape=(batches, output_height, output_width, output_depth))
    for n in range(batches):
        result = []
        for h_idx in range(output_height):
            for w_idx in range(output_width):
                temp_input = input_data[n, h_idx:h_idx + kernel_height, w_idx:w_idx + kernel_width]
                temp_input = np.expand_dims(temp_input, axis=0)
                temp_kernel = np.transpose(filter_data, (3, 0, 1, 2))
                temp_output = temp_input * temp_kernel
                # print(temp_output.shape)
                # print(temp_output.reshape(output_depth, -1).shape)
                temp_output = temp_output.reshape(output_depth, -1).sum(axis=-1)
                # print(dd.sum(axis=-1).shape)

                # exit()
                # print(temp_output.sum().shape)
                # print(temp_output.sum())
                # exit()
                # result.append(temp_output.sum(axis=0))
                # result.append(temp_output.sum())
                result.append(temp_output)
        result = np.array(result)
        # print(result.shape)
        # exit()
        # result = np.transpose(result, (1, 0))  # HW, C
        result = result.reshape(output_height, output_width, output_depth)
        output[n] = result

    return output

input_data = np.zeros((2,4,4,3))
filter_data = np.zeros([3, 3, 3, 5])

# print(conv2d(input_data, filter_data))
print('out shape :', conv2d(input_data, filter_data).shape)
